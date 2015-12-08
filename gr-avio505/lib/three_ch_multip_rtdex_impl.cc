/* -*- c++ -*- */
/* 
 * Copyright 2015 <+YOU OR YOUR COMPANY+>.
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
#include "three_ch_multip_rtdex_impl.h"

#include <volk/volk.h>

#include <functional>   // std::bit_xor
 

 

using namespace std;


namespace gr {
  namespace avio505 {

    three_ch_multip_rtdex::sptr
    three_ch_multip_rtdex::make()
    {
      return gnuradio::get_initial_sptr
        (new three_ch_multip_rtdex_impl());
    }


    /*
     * The private constructor
     */
    three_ch_multip_rtdex_impl::three_ch_multip_rtdex_impl()
      : gr::block("three_ch_multip_rtdex",
              gr::io_signature::make3(3, 3, sizeof(gr_complex), sizeof(gr_complex), sizeof(gr_complex)),
              gr::io_signature::make(1, 1, sizeof(short)))
    {
      const int alignment_multiple = 
              volk_get_alignment() / sizeof(short);
      set_alignment(std::max(1, alignment_multiple));
      // flag_start =   0;  //61440;
      flag_start =  61440;
      // clear_first4bits = 65535;
      clear_first4bits = 4095;
      dme1_shorts = (short*)volk_malloc(sizeof(short)*16384*2,  alignment_multiple   );
      dme2_shorts = (short*)volk_malloc(sizeof(short)*16384*2,  alignment_multiple   );
      adsb_shorts = (short*)volk_malloc(sizeof(short)*16384*8,  alignment_multiple   );

    }

    /*++q                                                                                                                                                                                         
     * Our virtual destructor.
     */
    three_ch_multip_rtdex_impl::~three_ch_multip_rtdex_impl()
    {
    }

    void
    three_ch_multip_rtdex_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
        /* <+forecast+> e.g. */
      ninput_items_required[0] = int( ceil(noutput_items/12.0) )  ;
      ninput_items_required[1] = ninput_items_required[0] ;
      ninput_items_required[2] = ninput_items_required[0]*4 ;
    }

    int
    three_ch_multip_rtdex_impl::general_work (int noutput_items,
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


        int escala = 2047;
        int nin_to_process = int( floor(noutput_items/12.0) );
        int nout_generated = nin_to_process*12;

        volk_32f_s32f_convert_16i(dme1_shorts, dme1_floats, escala , nin_to_process*2);
        volk_32f_s32f_convert_16i(dme2_shorts, dme2_floats, escala , nin_to_process*2);
        volk_32f_s32f_convert_16i(adsb_shorts, adsb_floats, escala , nin_to_process*8);



        for( int i = 0; i < nin_to_process; i++ ){
          out[i*12]    = dme1_shorts[i*2]|flag_start;
          out[i*12+1]  = dme1_shorts[i*2+1]&clear_first4bits;
          out[i*12+2]  = dme2_shorts[i*2]&clear_first4bits;
          out[i*12+3]  = dme2_shorts[i*2+1]&clear_first4bits; 

          out[i*12+4]  = adsb_shorts[i*8]&clear_first4bits;
          out[i*12+5]  = adsb_shorts[i*8 + 1]&clear_first4bits;          
          out[i*12+6]  = adsb_shorts[i*8 + 2]&clear_first4bits;
          out[i*12+7]  = adsb_shorts[i*8 + 3]&clear_first4bits;          
          out[i*12+8]  = adsb_shorts[i*8 + 4]&clear_first4bits;
          out[i*12+9]  = adsb_shorts[i*8 + 5]&clear_first4bits;          
          out[i*12+10] = adsb_shorts[i*8 + 6]&clear_first4bits;
          out[i*12+11] = adsb_shorts[i*8 + 7]&clear_first4bits;
        }
        //cout <<  << endl;

        // if( noutput_items  >= 1024)
        
        /*{

          cout << 
        "Nout \t" << noutput_items << "\t ninputes= " << ninput_items[0]<< 
           "\t" << ninput_items[1]<< "   "<< ninput_items[2]<< "\n"; 

        cout <<   "nin_to_process= " << nin_to_process <<  
        "\tnout_generated= " << nout_generated << endl; 
        // for( int oo = 0 ; oo < 64 ; oo ++) {
        //     cout << oo << fixed << "= \t" << in_dme1[oo] <<  " \t" 
        //     << dme1_floats[oo*2] << "   " <<  dme1_floats[oo*2 + 1]<<  " \t" 
        //     << dme1_shorts[oo*2] << "   " <<  dme1_shorts[oo*2 + 1]<<  " \t"
        //     << dme1_floats[oo*2]*escala << "   " <<  dme1_floats[oo*2 + 1]*escala <<  " \t" 
        //     << endl;

        // } 
        cout << "\n\n\n";
        }
        */

      // short aa = 0;
      // unsigned short bb = 61440;
      // short cc;
      // cc =   aa^bb ;
      //  cout << "xores" <<  cc << endl;


        // Do <+signal processing+>
        // Tell runtime system how many input items we consumed on
        // each input stream.
        consume(0, nin_to_process );
        consume(1, nin_to_process   );
        consume(2, nin_to_process*4 );
        

        // Tell runtime system how many output items we produced.
        return nout_generated;
    }

  } /* namespace avio505 */
} /* namespace gr */