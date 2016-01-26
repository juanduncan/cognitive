/* -*- c++ -*- */
/* 
 * Copyright 2016 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "three_ch_mux_rtdex_v2_impl.h"

#include <volk/volk.h>

#include <functional>   // std::bit_xor
 

 

using namespace std;



namespace gr {
  namespace avio505 {

    three_ch_mux_rtdex_v2::sptr
    three_ch_mux_rtdex_v2::make()
    {
	  int xxxx[] = {8,8,8};
	  std::vector<int> sizeof_stream_items( xxxx, xxxx + sizeof(xxxx)/ sizeof(xxxx[0])   );
      return gnuradio::get_initial_sptr
        (new three_ch_mux_rtdex_v2_impl(sizeof_stream_items));
    }

    /*
     * The private constructor
     */
    three_ch_mux_rtdex_v2_impl::three_ch_mux_rtdex_v2_impl(std::vector<int> sizeof_stream_items)
      :gr::block("AVIO505 DAC MUX",
              gr::io_signature::makev(3, 3, sizeof_stream_items),
              gr::io_signature::make(1, 1, sizeof(int))
              )
    {
      const int alignment_multiple = 
      volk_get_alignment() / sizeof(short);
      set_alignment(std::max(1, alignment_multiple));
      // flag_start =   0;  //61440;
      flag_start =  1;
      // clear_bits = 65535;
      clear_bits = 0xfffe;
      dme1_shorts = (short*)volk_malloc(sizeof(short)*16384*2,  alignment_multiple   );
      dme2_shorts = (short*)volk_malloc(sizeof(short)*16384*2,  alignment_multiple   );
      adsb_shorts = (short*)volk_malloc(sizeof(short)*16384*8,  alignment_multiple   );
		}

    /*
     * Our virtual destructor.
     */
    three_ch_mux_rtdex_v2_impl::~three_ch_mux_rtdex_v2_impl()
    {
    }

    void
    three_ch_mux_rtdex_v2_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      ninput_items_required[0] = int( ceil(noutput_items/6.0) )  ;
      ninput_items_required[1] = ninput_items_required[0] ;
      ninput_items_required[2] = ninput_items_required[0]*4 ;
    }

    int
    three_ch_mux_rtdex_v2_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
        const gr_complex *in_dme1 = (const gr_complex*) input_items[0];
        const gr_complex *in_dme2 = (const gr_complex*) input_items[1];
        const gr_complex *in_adsb = (const gr_complex*) input_items[2];
        
        short *out = (short *) output_items[0];

        dme1_floats = (float*)in_dme1;
        dme2_floats = (float*)in_dme2;
        adsb_floats = (float*)in_adsb;


        int escala = 32767;
        int nin_to_process = int( floor(noutput_items/6.0) );
        int nout_generated = nin_to_process*6;

        volk_32f_s32f_convert_16i(dme1_shorts, dme1_floats, escala , nin_to_process*2);
        volk_32f_s32f_convert_16i(dme2_shorts, dme2_floats, escala , nin_to_process*2);
        volk_32f_s32f_convert_16i(adsb_shorts, adsb_floats, escala , nin_to_process*8);

        out_shorts = (short*)out;
		int index_out = 0;
		int index_dme = 0;
		int index_adsb = 0;
		
        for( int i = 0; i < nin_to_process; i++ ){
          out_shorts[index_out]     = dme1_shorts[index_dme]|flag_start;
          out_shorts[index_out+1]   = dme1_shorts[index_dme+1]&clear_bits;
          out_shorts[index_out+2]   = dme2_shorts[index_dme]&clear_bits;
          out_shorts[index_out+3]   = dme2_shorts[index_dme+1]&clear_bits; 

          out_shorts[index_out+4]   = adsb_shorts[index_adsb    ]&clear_bits;
          out_shorts[index_out+5]   = adsb_shorts[index_adsb + 1]&clear_bits;          
          out_shorts[index_out+6]   = adsb_shorts[index_adsb + 2]&clear_bits;
          out_shorts[index_out+7]   = adsb_shorts[index_adsb + 3]&clear_bits;          
          out_shorts[index_out+8]   = adsb_shorts[index_adsb + 4]&clear_bits;
          out_shorts[index_out+9]   = adsb_shorts[index_adsb + 5]&clear_bits;          
          out_shorts[index_out+10]  = adsb_shorts[index_adsb + 6]&clear_bits;
          out_shorts[index_out+11]  = adsb_shorts[index_adsb + 7]&clear_bits;
          
          index_out+=12;
          index_dme+=2;
          index_adsb+=8;
        }

        consume(0, nin_to_process );
        consume(1, nin_to_process );
        consume(2, nin_to_process*4 );

        // Tell runtime system how many output items we produced.
        return nout_generated;
    }

  } /* namespace avio505 */
} /* namespace gr */



