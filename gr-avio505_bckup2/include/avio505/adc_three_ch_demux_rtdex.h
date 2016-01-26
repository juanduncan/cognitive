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


#ifndef INCLUDED_AVIO505_ADC_THREE_CH_DEMUX_RTDEX_H
#define INCLUDED_AVIO505_ADC_THREE_CH_DEMUX_RTDEX_H

#include <avio505/api.h>
#include <gnuradio/block.h>

namespace gr {
  namespace avio505 {

    /*!
     * \brief <+description of block+>
     * \ingroup avio505
     *
     */
    class AVIO505_API adc_three_ch_demux_rtdex : virtual public gr::block
    {
     public:
      typedef boost::shared_ptr<adc_three_ch_demux_rtdex> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of avio505::adc_three_ch_demux_rtdex.
       *
       * To avoid accidental use of raw pointers, avio505::adc_three_ch_demux_rtdex's
       * constructor is in a private implementation
       * class. avio505::adc_three_ch_demux_rtdex::make is the public interface for
       * creating new instances.
       */
      static sptr make();
    };

  } // namespace avio505
} // namespace gr

#endif /* INCLUDED_AVIO505_ADC_THREE_CH_DEMUX_RTDEX_H */

